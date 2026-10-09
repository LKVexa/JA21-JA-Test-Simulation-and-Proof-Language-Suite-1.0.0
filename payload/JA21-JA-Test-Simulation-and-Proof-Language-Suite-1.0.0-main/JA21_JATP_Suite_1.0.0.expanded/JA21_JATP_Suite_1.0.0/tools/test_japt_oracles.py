"""Verify fixture/property separation and provenance; no native JA runtime runs."""
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_ARCHIVE = Path(r'D:\desktop\LKVexa Dictionary\JA21-JA-Test-Simulation-and-Proof-Language-Suite-1.0.0-main.zip')


class CountOracleRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with gzip.open(ROOT / 'corpus/technical/JA21_JATP_TECHNICAL_CORPUS_10000.jsonl.gz', 'rt', encoding='utf-8') as stream:
            cls.records = [json.loads(line) for line in stream if line.strip()]
        cls.by_id = {r['record_id']: r for r in cls.records}
        with zipfile.ZipFile(ORIGINAL_ARCHIVE) as outer:
            inner = next(name for name in outer.namelist() if name.endswith('.zip'))
            with zipfile.ZipFile(io.BytesIO(outer.read(inner))) as suite:
                name = next(name for name in suite.namelist() if name.endswith('JA21_JATP_TECHNICAL_CORPUS_10000.jsonl.gz'))
                cls.original = {r['record_id']: r for r in (json.loads(line) for line in gzip.decompress(suite.read(name)).splitlines() if line.strip())}

    def test_original_fixture_constants_and_independent_oracle(self):
        checked = 0
        for r in self.records:
            if r['validation_result']['expected_status'] != 'pass':
                continue
            fixture = re.search(r'fixture (FixtureJATP_\d+)\s*\{\s*input (\d+)\s*expected (\d+)\s*\}', r['source'])
            original_fixture = re.search(r'fixture (FixtureJATP_\d+)\s*\{\s*input (\d+)\s*expected (\d+)\s*\}', self.original[r['record_id']]['source'])
            self.assertEqual(fixture.groups(), original_fixture.groups())
            name, input_value, expected_value = fixture.groups()
            test = re.search(r'unit test FixtureCheckJATP_\d+\s*\{\s*let fixture_result = ' + name + r'\.input \* (\d+)\s*assert fixture_result == ' + name + r'\.expected\s*\}', r['source'])
            self.assertIsNotNone(test, r['record_id'])
            multiplier = int(test.group(1))
            n, expected = int(input_value), int(expected_value)
            # Explicit nonnegative integer interpretation of these Count examples.
            self.assertEqual(n * multiplier, expected)
            self.assertNotEqual(n * (multiplier + 1), expected)
            self.assertNotIn('assert result == x *', r['source'])
            checked += 1
        self.assertEqual(checked, 7500)

    def test_quantified_property_contains_actual_invariant(self):
        values = 0
        for r in self.records:
            if r['validation_result']['expected_status'] != 'pass':
                continue
            property_match = re.search(r'property PropertyJATP_\d+ for_all x: Count where x <= (\d+)\s*\{\s*let result = x \* (\d+)\s*invariant result >= x\s*\}', r['source'])
            self.assertIsNotNone(property_match, r['record_id'])
            bound, multiplier = map(int, property_match.groups())
            for x in range(bound + 1):
                self.assertGreaterEqual(x * multiplier, x)
                values += 1
        self.assertEqual(values, 382297)

    def test_deliberately_failing_source_is_unchanged(self):
        unchanged = 0
        for r in self.records:
            if r['validation_result']['expected_status'] != 'pass':
                self.assertEqual(r['source'], self.original[r['record_id']]['source'])
                unchanged += 1
        self.assertEqual(unchanged, 2500)

    def test_source_hashes_and_qualifications(self):
        for r in self.records:
            digest = hashlib.sha256(r['source'].encode('utf-8')).hexdigest()
            self.assertEqual(r['ast']['origin_hash'], digest)
            self.assertEqual(r['_audit_qualification']['source_sha256'], digest)
            self.assertTrue(r['_audit_qualification']['source_hash_verified'])
            self.assertFalse(r['_audit_qualification']['native_execution_eligible'])
            self.assertIsNone(r['_audit_qualification']['observed_result'])

    def test_shard_and_script_consistency(self):
        count = 0
        for path in (ROOT / 'corpus/technical/shards').glob('*.jsonl.gz'):
            with gzip.open(path, 'rt', encoding='utf-8') as stream:
                for line in stream:
                    r = json.loads(line)
                    self.assertEqual(r, self.by_id[r['record_id']])
                    count += 1
        self.assertEqual(count, 10000)
        with (ROOT / 'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8', newline='') as stream:
            catalog = list(csv.DictReader(stream))
        self.assertEqual(len(catalog), 1000)
        for row in catalog:
            source = (ROOT / row['file']).read_text(encoding='utf-8')
            self.assertEqual(source, self.by_id[row['record_id']]['source'])
            self.assertEqual(hashlib.sha256(source.encode('utf-8')).hexdigest(), row['source_sha256'])


if __name__ == '__main__':
    unittest.main()
