import frelatage
import AdvancedHTMLParser


def test_html_parsing(html):
    parser = AdvancedHTMLParser.AdvancedHTMLParser()
    parser.parseStr(html)
    parser.getHTML()

input = frelatage.Input(value="<p>Some<b>bad<i>HTML")
f = frelatage.Fuzzer(test_html_parsing, [[input]], infinite_fuzz=True)
f.fuzz()