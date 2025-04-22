# Lily58 Wireless ZMK Config

這是針對 Lily58 無線鍵盤的 ZMK 設定檔案，包含多層鍵盤映射、無線配置以及相關的建置設定。

## 項目結構
- **`config/`**: 包含鍵盤配置檔案（如 `lily58.keymap`、`lily58.conf` 和 `west.yml`）。
- **`IMG/`**: 包含鍵盤圖片。
- **`.github/workflows/`**: 包含 CI/CD 工作流程設定。
- **`build.yaml`**: 定義建置設定。

## 鍵盤圖片
<div style="width: 80%; margin: auto;">
  <img src="https://github.com/cloverdefa/lily58-wireless-view-zmk-config/blob/main/IMG/lily58.jpg" style="width: 100%; height: auto;" alt="Lily58 Keyboard">
</div>

## 功能特色
- **多層鍵盤映射**: 支援 Windows、MacOS、遊戲模式等多層配置。
- **無線配置**: 支援 Nice!Nano V2 和 Nice!View 顯示模組。
- **深度睡眠模式**: 節省電力，支援 30 分鐘後進入深度睡眠。
- **自動建置與合併**: 使用 GitHub Actions 自動化建置與合併流程。

## 如何使用
1. 克隆此專案：
   ```bash
   git clone https://github.com/cloverdefa/lily58-wireless-view-zmk-config.git

   ```
2. 根據需求修改 config/lily58.keymap 和 config/lily58.conf。
   使用 ZMK 的建置工具建置韌體

3. 使用 ZMK 的建置工具建置韌體：
   ```bash
   west build -b nice_nano_v2 -- -DSHIELD=lily58_left
   west build -b nice_nano_v2 -- -DSHIELD=lily58_right
   ```

4. 將生成的韌體燒錄到 Nice!Nano V2。


貢獻
歡迎提交 Issue 或 Pull Request 來改進此專案。

授權
此專案基於 MIT 授權條款，詳見 [LICENSE](https://github.com/cloverdefa/lily58-wireless-view-zmk-config/blob/main/LICENSE.md) 文件。