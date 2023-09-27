import pytest
import yaml
from checks import checkout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:
    def test_step1(self, make_folders, clear_folders, make_files, print_time):
        res1 = checkout("cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"],
                                                         data["type"]), "Everything is Ok")
        res2 = checkout("ls {}".format(data["folder_out"]), "arx.{}".format(data["type"]))
        assert res1 and res2, "test1 FAIL"

    def test_step2(self, clear_folders, make_files):
        res = []
        res.append(checkout("cd {}; 7z a {}/arx -t{}".format(data["folder_in"], data["folder_out"],
                                                             data["type"]), "Everything is Ok"))
        res.append(checkout("cd {}; 7z e arx.{} -o{} -y".format(data["folder_out"], data["type"],
                                                                data["folder_ext"]), "Everything is Ok"))
        for item in make_files:
            res.append(checkout("ls {}".format(data["folder_ext"]), item))
        assert all(res)

    def test_step3(self):
        assert checkout("cd {}; 7z t arx.{}".format(data["folder_out"], data["type"]),
                        "Everything is Ok"), "test3 FAIL"


if __name__ == '__main__':
    pytest.main(['-vv'])
