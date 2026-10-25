# Lily58 Wireless ZMK Config

這是 Lily58 無線分體鍵盤的 [ZMK](https://zmk.dev/) 設定。韌體目標為左右兩側的 nice!nano v2，並搭配 nice!view 顯示器。

<p align="center">
  <img src="assets/lily58.jpg" width="80%" alt="Lily58 鍵盤">
</p>

## Keymap

`config/lily58.keymap` 定義 11 個鍵盤層：

| 層 | 用途 |
| --- | --- |
| Omarchy | Omarchy/Linux 日常輸入與快捷鍵 |
| OmcNav | 導航、功能鍵、媒體控制與滑鼠層入口 |
| OmcCode | 符號、tmux 快捷鍵 |
| OmcFunc | 功能鍵與系統／滑鼠層入口 |
| MacOS | macOS 日常輸入與快捷鍵 |
| MacNav | 導航、功能鍵、媒體控制與滑鼠層入口 |
| MacCode | 符號、tmux 與視窗快捷鍵 |
| MacFunc | 功能鍵與系統／滑鼠層入口 |
| Mouse | 指標移動、捲動、滑鼠按鍵 |
| Game | 遊戲用按鍵配置 |
| System | 藍牙配對槽、清除配對、重啟與 bootloader |

Nav 和 Code 層同時啟用時，會自動啟用對應的 Func 層。拇指鍵提供層切換、修飾鍵與常用按鍵。Keymap 也包含中文輸入法、終端機、視窗管理及 tmux 等快捷鍵巨集；部分巨集依賴主機端的作業系統或軟體快捷鍵設定。

## 無線、睡眠與指標設定

`config/lily58.conf` 設定裝置名稱為 `Lily58`、啟用 ZMK sleep 與 pointing，並調整藍牙連線間隔、背景掃描及按鍵去彈跳時間。閒置 900,000 毫秒（15 分鐘）後進入睡眠。

ZMK Studio 目前未啟用；`CONFIG_ZMK_STUDIO` 與 Studio USB-UART snippet 都是註解狀態。

## 專案檔案

- `config/lily58.keymap`：layers、behaviors 與快捷鍵巨集。
- `config/lily58.conf`：ZMK Kconfig 設定。
- `config/west.yml`：West manifest，使用 ZMK `v0.3`。
- `build.yaml`：左右兩側的 nice!nano v2 建置目標，皆包含 nice!view adapter 與顯示器 shield。
- `IMG/`：鍵盤照片與 keymap SVG。
- `main.py`：使用 `keymap` CLI 從 keymap 產生 `IMG/lily58.svg`。

## 建置韌體

在已安裝 ZMK 開發工具鏈的環境中，於 repo 根目錄初始化並更新 West workspace：

```sh
west init -l config
west update
```

建置左右兩側：

```sh
west build -p=auto -d build/left -b nice_nano_v2 -- \
  -DSHIELD="lily58_left nice_view_adapter nice_view"

west build -p=auto -d build/right -b nice_nano_v2 -- \
  -DSHIELD="lily58_right nice_view_adapter nice_view"
```

建置產物位於各自的 build 目錄。也可以使用 repo 根目錄的 `build.yaml` 作為支援該設定檔的 ZMK 建置流程輸入。此 repo 目前沒有包含 `.github/workflows/`，因此韌體不會由本 repo 內的 GitHub Actions workflow 自動建置。

## 更新鍵盤圖

`main.py` 需要 `keymap` CLI 可從 PATH 執行。安裝並設定好該工具後，在 repo 根目錄執行：

```sh
python3 main.py
```

腳本會解析 `config/lily58.keymap`，更新 `IMG/lily58.svg`，並刪除中間產生的 YAML 檔案。

## 系統層操作

在 System 層可使用 `BT_CLR` 清除藍牙配對，使用 `BT_SEL 0` 至 `BT_SEL 4` 選擇配對槽；另有 `sys_reset` 重啟與 `bootloader` 進入 bootloader 的按鍵。

## 授權

本專案採用 MIT License，詳見 [LICENSE.md](LICENSE.md)。
