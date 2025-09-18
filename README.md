# Lily58 Wireless ZMK Config

此倉庫為 Lily58 無線鍵盤的 ZMK 設定，包含多層 keymap、無線設定與 CI 建置流程。

## 專案結構

- `config/`: 主要設定（`lily58.keymap`、`lily58.conf`、`west.yml`）。
- `IMG/`: 鍵盤/佈局相關圖片資產。
- `.github/workflows/`: CI 建置流程。
- `build.yaml`: CI 建置矩陣（左右半部與顯示模組）。

## 功能特色

- 多層鍵盤映射：支援 Windows / macOS / 遊戲等層。
- 無線配置：支援 Nice!Nano V2 與 Nice!View 顯示模組。
- 省電：深度睡眠，預設 30 分鐘後進入。
- CI 自動化：GitHub Actions 產出左右半部韌體。

## 建置與使用

1) 初始化 ZMK 工作區（於此倉庫根目錄）：

```bash
west init -l config
west update
```

2) 本機建置左右半部（輸出位於 `build/<side>/zephyr/zmk.uf2`）：

```bash
west build -d build/left  -b nice_nano_v2 -- -DSHIELD=lily58_left
west build -d build/right -b nice_nano_v2 -- -DSHIELD=lily58_right
```

3) 將產生之 `zmk.uf2` 分別燒錄到左右半部的 Nice!Nano V2。

4) 依需求調整 `config/lily58.keymap` 與 `config/lily58.conf`，重新建置驗證。

## 測試與 CI

- 確認左右半部皆可成功建置並產生 `zmk.uf2`。
- 重大變更請附 keymap 差異或對照圖（可放於 `IMG/`）。
- CI 會依 `build.yaml` 定義的矩陣建置左右半部與顯示模組。
- 請勿提交產物與私密資料（`build/`、`.uf2`、序號/金鑰）。

## 鍵盤圖片

<div style="width: 80%; margin: auto;">
  <img src="IMG/lily58.jpg" style="width: 100%; height: auto;" alt="Lily58 Keyboard">
  <img src="IMG/lily58.svg" style="width: 100%; height: auto;" alt="Lily58 Keyboard SVG">
  
</div>

## 貢獻

- 建議採用 Conventional Commits（如 `ci:`、`build:`、`refactor:`）。
- 送 PR 前，請先於本機完成左右半部建置並附上重現指令。
- 詳見貢獻與風格規範：`AGENTS.md`。

## 授權

此專案採用 MIT 授權，詳見 `LICENSE.md`。
