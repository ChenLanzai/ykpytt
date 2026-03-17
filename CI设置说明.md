# 把 Pytest + Allure 接到 GitHub Actions（CI 设置说明）

本文说明如何让「自动测试 + 出报告」在每次推送代码时自动执行，即完成 CI 里的「自动测试 + 出报告」这一步。

---

## 一、你需要准备的东西

1. **代码在 GitHub 上**  
   项目在一个 Git 仓库里，并已推送到 GitHub（例如 `https://github.com/你的用户名/你的仓库名`）。

2. **项目里已有**  
   - 能本地跑通的 Pytest 用例（例如 `pytest -v --alluredir=allure-results`）。  
   - `requirements.txt`（包含 `pytest`、`allure-pytest` 等）。  
   - （可选）`pytest.ini` 里配置了 `--alluredir=allure-results`。

3. **不需要**  
   - 自己的服务器、自己的后端。  
   - 一定要有 GitHub Pages；没有也可以，报告可通过「Artifact 下载」查看。

---

## 二、在项目里加上 GitHub Actions 工作流

### 1. 创建 workflow 文件

在项目根目录下新建目录和文件（注意大小写）：

```
.github/
  workflows/
    ci-pytest-allure.yml
```

即：`.github/workflows/ci-pytest-allure.yml`。

### 2. 文件内容

`ci-pytest-allure.yml` 的内容见下一节「三、工作流文件示例」；复制进去保存即可。

### 3. 提交并推送

```bash
git add .github/workflows/ci-pytest-allure.yml
git commit -m "ci: add pytest + allure workflow"
git push origin main
```

（若主分支叫 `master`，把 `main` 改成 `master`。）

---

## 三、工作流文件示例

下面是一份「只做：自动测试 + 出 Allure 报告」的 CI 配置；可选：上传报告为 Artifact、或部署到 GitHub Pages。

- **触发**：每次推送到 `main` / `master`（以及可选 PR）。  
- **步骤**：拉代码 → 装 Python → 装依赖 → 装 Allure CLI → 跑 Pytest（结果写到 `allure-results`）→ 用 Allure 生成报告 → 上传报告为 Artifact；如需在线看，再部署到 GitHub Pages。

已按你当前项目结构写好的文件在：`.github/workflows/ci-pytest-allure.yml`（见本仓库该路径）。你只需确认该文件存在并推送到 GitHub 即可。

若你的项目**需要 .env**（例如 `SERVER_URL`、`PUBLIC_KEY`），在 GitHub 仓库里：

1. 打开仓库 → **Settings** → **Secrets and variables** → **Actions**。  
2. 新建 Repository secrets：`SERVER_URL`、`PUBLIC_KEY`（值填你的测试环境地址和公钥）。  
3. 工作流里已有「用 secrets 生成 .env」的步骤时，CI 会用这些值跑用例。

若项目**不需要 .env**（例如只测 JSONPlaceholder），可删掉或注释掉工作流里「生成 .env」的那一步。

---

## 四、推送后怎么查看结果

1. 打开 GitHub 仓库页面。  
2. 点顶栏 **Actions**。  
3. 左侧选中你用的 workflow 名字（如 **CI - Pytest + Allure**）。  
4. 点最近一次运行（由 push 触发）。  
5. 看 **Jobs** 里的 `test`：  
   - **绿色勾**：步骤都成功（含 Pytest 通过）。  
   - **红叉**：某步失败（常见为 Pytest 失败或依赖缺失）；点进该 Job 看具体报错。  
6. **下载 Allure 报告**：在同一 Run 页面右侧 **Artifacts** 里下载 `allure-report`，解压后打开其中的 `index.html` 查看。  
7. **在线看报告（需已开启 GitHub Pages）**：在仓库 **Settings** → **Pages** 里把 Source 设为「GitHub Actions」；工作流里若配置了 deploy，报告会发布到 `https://你的用户名.github.io/你的仓库名/`。

---

## 五、小结

| 步骤 | 你要做的 |
|------|-----------|
| 1 | 在项目里建 `.github/workflows/ci-pytest-allure.yml`（内容见仓库内该文件）。 |
| 2 | 如需 .env，在仓库 Settings → Secrets 里配好 `SERVER_URL`、`PUBLIC_KEY`。 |
| 3 | `git add` → `commit` → `push` 到 GitHub。 |
| 4 | 到 **Actions** 看运行结果，在 **Artifacts** 下载报告；可选开启 Pages 在线看。 |

这样，「现在的 Pytest + Allure」就接进了 GitHub Actions，完成 CI 里的「自动测试 + 出报告」这一步。
