pythonのクラスや関数を勉強してAPIを使いやすくできないか試したモノです。
MITライセンスになっていますが、データに関する権限についてはさけのわデータプロジェクト様に準拠します。

# 使用データ

## さけのわデータプロジェクト
日本酒アプリさけのわが保有するフレーバーを数値化したデータや人気銘柄情報を公開するプロジェクト

https://muro.sakenowa.com/sakenowa-data/

## データの種類
>さけのわではユーザーの感想コメントを解析してフレーバーを数値化しています。このデータに加えてランキング情報を含む以下のデータを公開します。
>銘柄ごとのフレーバーを華やか、芳醇、重厚、穏やか、軽快、ドライの6つの観点で数値化したもの
>- 銘柄ごとのフレーバーの詳細をタグ化したもの (フレーバータグ)
>- さけのわでの人気銘柄ランキング
>- その他、銘柄の基本情報

## エンドポイント
- 地域一覧 (/api/areas)
- 銘柄一覧 (/api/brands)
- 蔵元一覧 (/api/breweries)
- ランキング (/api/rankings)
- フレーバーチャート (/api/flavor-charts)
- フレーバータグ一覧 (/api/flavor-tags)
- 銘柄ごとのフレーバータグ (/api/brand-flavor-tags)

# 試し方

- このリポジトリを git cloneする

- 初回起動（次回以降 --buildは無くて良い）
`docker-compose up -d --build`

- コンテナ終了
`docker-compose down`

- コンテナの中で作業する
`docker exec -it sakenowa_sandbox_1 /bin/bash`

以降コンテナ内で実行
- sakenowaのお試しコードの実行
`python src/test_sakenowa.py`

- sakenowa フレーバーチャートの作成
`python src/test_radar_chart.py`

# 参考URL
[さけのわデータプロジェクト](https://muro.sakenowa.com/sakenowa-data/)
[Pythonでゆるく始める静的型検査](https://qiita.com/ocknamo/items/6341d0a7757c668782c8#%E3%81%8A%E3%81%BE%E3%81%91stub%E3%82%92%E8%87%AA%E5%8B%95%E7%94%9F%E6%88%90%E3%81%99%E3%82%8B)
[Matplotlibでレーダーチャートを描く（16行）](https://qiita.com/1007/items/80406e098a4212571b2e)
