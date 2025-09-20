# Repository Guidelines

本文件為此 ZMK 設定庫（Lily58 無線）之貢獻指南，協助你快速熟悉結構、建置與提交流程。

## 作用範圍與優先序

- 作用範圍：此文件適用於本倉庫的整個目錄樹。
- 優先序：如子目錄另有 `AGENTS.md`，則以較深層者為準；若與明確的專案指示衝突，則以專案指示為準。

## 專案結構與模組組織

- `config/`: 主要設定（`lily58.keymap`、`lily58.conf`、`west.yml`）。
- `IMG/`: 鍵盤/佈局相關圖片資產。
- `.github/workflows/`: CI 建置流程。
- `build.yaml`: CI 建置矩陣（左右半部與顯示模組）。

## 建置、測試與開發指令

首次建置（會抓取 ZMK 專案並建立工作區）：

```bash
west init -l config
west update
```

本機分別建置左右半部（輸出位於 `build/<side>/zephyr/zmk.uf2`）：

```bash
west build -d build/left  -b nice_nano_v2 -- -DSHIELD=lily58_left
west build -d build/right -b nice_nano_v2 -- -DSHIELD=lily58_right
```

常用：乾淨重建 `-p`、只換目標 `-t`：

```bash
west build -p=auto -d build/left  -b nice_nano_v2 -- -DSHIELD=lily58_left
west build -p=auto -d build/right -b nice_nano_v2 -- -DSHIELD=lily58_right
```

含 Nice!View 與 ZMK Studio（與 `build.yaml` 一致）：

```bash
west build -p=auto -d build/left  -b nice_nano_v2 -- \
  -DSHIELD="lily58_left nice_view_adapter nice_view" \
  -DSNIPPET=studio-rpc-usb-uart

west build -p=auto -d build/right -b nice_nano_v2 -- \
  -DSHIELD="lily58_right nice_view_adapter nice_view"
```

## 程式風格與命名規範

- 縮排：YAML 2 空白；`.keymap`/`.conf` 以 2 空白對齊區塊。
- 檔名：鍵盤/板定義使用小寫與中線或底線（例：`lily58.keymap`）。
- 層名稱：使用全大寫（例：`BASE`、`NAV`、`GAME`）。
- 設定鍵（`.conf`）使用既有 `CONFIG_` 開關，不自創前綴。

## 測試指引

- 必須保證左右半部皆可成功建置且產生 `zmk.uf2`。
- 重大變更請附上新舊層級對照（可放在 `IMG/`）或片段 keymap 差異。
- 提交前確保 CI 綠燈；本機請先跑兩側建置以復現。

## Commit 與 Pull Request 規範

- 建議採用 Conventional Commits（本庫歷史含有 `ci:`、`build:`、`refactor:`）。
  - 範例：`ci: 調整 Actions 觸發條件`、`build: 新增 nice_view 設定`。
- PR 需包含：
  - 變更摘要與動機、影響層級（列出新增/調整之層）。
  - 關聯 issue（如有）、截圖或對應 `IMG/` 圖片。
  - 本機建置結果（左右半部）與重現指令。

## 安全與設定提示

- 請勿提交產物與私密資料（`build/`、`.uf2`、序號/金鑰）。
- 變更 `west.yml` 或 `build.yaml` 前，確認 CI 矩陣仍涵蓋左右半部與顯示模組。
- Studio Snippet 僅需在左半部啟用（USB-UART），與現行 `build.yaml` 一致。

## 代理（AI 助理）補充

- 修改檔案時維持最小變更，遵循本檔案之縮排與命名規範。
- 讀取專案時以 `rg` 搜尋並分段閱讀，避免過長輸出。
- 需要新增/調整建置流程時，先於本機驗證左右半部能產出 `zmk.uf2`。
- 僅在必要時調整 `build.yaml` 或 `west.yml`，並說明影響範圍。
- 不提交產物、金鑰或序號等敏感資訊；避免將 `build/` 目錄納入版本控制。
