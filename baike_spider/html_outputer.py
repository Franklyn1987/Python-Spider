# coding=utf-8


class HtmlOutputer:
    def __init__(self):
        self.datas = []

    def collectData(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('/Users/wang/Desktop/output.html', 'w')

        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title_node'].encode(encoding='UTF-8'))
            fout.write('<td>%s</td>' % data['summary_node'].encode(encoding='UTF-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
