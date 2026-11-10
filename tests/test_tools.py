import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'tools' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class SafetyTests(unittest.TestCase):
    def test_unrecognized_firmware_is_rejected(self):
        patch = module('patch_apps_common')
        for reverse in (False, True):
            with self.assertRaises(ValueError):
                patch.transform(bytes(30000), reverse=reverse)

    def test_protected_application_cannot_be_disabled(self):
        generator = module('generate_cleanup')
        profile = json.loads((ROOT / 'profiles/bu8000-1720.7.json').read_text())
        profile['groups']['acr'].append(profile['protected_apps'][0])
        with self.assertRaises(ValueError):
            generator.generate(profile)

    def test_profile_cannot_inject_shell_commands(self):
        generator = module('generate_cleanup')
        profile = json.loads((ROOT / 'profiles/bu8000-1720.7.json').read_text())
        profile['runtime_units'][0] = 'test; touch /tmp/unwanted'
        with self.assertRaises(ValueError):
            generator.generate(profile)


if __name__ == '__main__':
    unittest.main()
