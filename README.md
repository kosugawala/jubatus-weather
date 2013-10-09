==========
 天気分類
==========

天気は日々変化します。しかし「夏は蒸し暑く冬は寒くて乾燥している」など、天気には季節により大まかな傾向があるのでそこに注目することで分類が可能です。


準備
====

- Jubauts 0.4.0 以上 + Python クライアントをインストールします  ([公式ページ](http://jubat.us/ja/quickstart.html))



サーバーの起動
==============

jubaclassifier を起動します

```
 $ jubaclassifier -f weather.json
```


インストール
====

コマンドラインアプリケーションをインストールして利用します。

インストールはsetup.pyのあるディレクトリに移動して作業して下さい。

```
 $ cd python
 $ python setup.py install
```
インストールが終了すると python/build/ python/dist/ python/jubaweather.egg-info が作成されます。 


実行
====

dat/weather_train.csv は気象庁から取得した「2008年1月から2012年12月までの過去5年間の日別気象情報」です。日平均気温(℃)、日最高気温(℃)、日最低気温(℃)、日平均蒸気圧(hPa)、日平均相対湿度(%)をパラメータとして使用し、時期（9月上旬, 12月中旬 など）を学習させています。

dat/weather_train.csv を学習し、 dat/weather.yml に記載した条件の日の天気がいつ頃のものか分類しましょう。

```
  $ jubaweather -t dat/weather_train.csv -a dat/weather.yml
```

dat/weather.yml を変更し、色々な条件でその日の天気の時期を分類出来ます。

```
  $ edit dat/weather.yml
  $ jubaweather -a dat/weather.yml
  $ edit dat/weather.yml
  $ jubahomes -a dat/weather.yml
     :
```

プログラムを修正し他の気象条件を追加してみてはいかがでしょうか。

出力例
====

実際の日付に続き、分類結果がスコアの高い順に5つ出力されます。

```
2010-06-15 ( mid June )
mid June 7.31312036514
late June 7.26367235184
late Oct. 7.23103094101
early Aug. 7.19889163971
late July 7.16241979599
     :
```
本プログラムでは/tmp/ 以下にjubatusのモデル情報を保存しています。[jubatus/jubadump](https://github.com/jubatus/jubadump)を用いることでモデルの重み付け情報を取得出来ます。

----
*本プロジェクトは[jubatus/jubatus-example](https://github.com/jubatus/jubatus-example)内のサン
プルを参考に作成いたしました*
