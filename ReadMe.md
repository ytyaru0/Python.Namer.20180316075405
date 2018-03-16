# このソフトウェアについて

単語間を区切る文字を統一する。

* [順序付最短名](https://github.com/ytyaru0/Python.NameGenerator.20180313180534)

# 表記法

case|例
----|--
camel|getSome, GetSome
snake|get_some, GET_SOME
chain|get-some, GET-SOME

# 実行

```sh
$ Namer.py
```
```sh
$ Namer.py -r camel -c upper get_some
GetSome
```

## 起動引数

### 位置引数

i|略|意味
-|--|----
0|{target}|対象の名前（文字列）

たとえば以下のような値を入力できる。

* `get_html`
* `get-html`
* `"get html"`
* `getHtml`
* `GetHtml`
* `GetHTMLParser`

ただし、camel, snake, chain, space, のどれにも当てはまらないと例外発生。

```
Exception: targetが不正値です。camel, snake, chain, space のいずれかに合わせた文字列にしてください。
```

### オプション

略|全|値
--|--|--
-r|--rule|camel, snake, chain, space
-c|--case|upper, lower, as-is

* as-isは強制変換せずそのまま
* spaceはおまけ。ふつう名前にspaceは入れない

#### ruleにおけるcaseのデフォルト値

rule|case
----|----
camel|upper
snake|lower
chain|lower

#### 出力例1

`getHTMLParser`, `get_html_parser`を入力したとき。

rule|lower|upper
----|-----|-----
camel|getHtmlParser|GetHtmlParser
snake|get_html_parser|GET_HTML_PARSER
chain|get-html-parser|GET-HTML-PARSER
space|get html parser|GET HTML PARSER

#### 出力例2

`getHTMLParser`を入力したとき。

rule|as-is
----|-----
camel|getHTMLParser
snake|get_HTML_Parser
chain|get-HTML-Parser
space|get HTML Parser

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000)
            * Python 3.6.4

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

