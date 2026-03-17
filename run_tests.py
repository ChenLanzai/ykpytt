# run_tests.py
import subprocess
import sys

if __name__ == "__main__":
    # 1. 跑用例，结果写入 allure-results
    r = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--alluredir=allure-results", "--clean-alluredir"],
        shell=False,
    )
    if r.returncode != 0:
        sys.exit(r.returncode)

    # 2. 生成 Allure 报告到 allure-report
    subprocess.run(
        ["allure", "generate", "allure-results", "-o", "allure-report", "--clean"],
        shell=True,
    )

    # 3. 自动打开报告（可选，不想自动打开可注释掉）
    subprocess.run(["allure", "open", "allure-report"], shell=True)
