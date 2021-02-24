import requests

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '31',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'UM_distinctid=177d1b0e1dd391-0184066ab6e227-73e356b-1fa400-177d1b0e1dec7f; CNZZDATA1261035915=450026094-1614128166-https%253A%252F%252Fwww.baidu.com%252F%7C1614128166',
    'Host': 'www.ceigle.com',
    'Origin': 'http://www.ceigle.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.ceigle.com/epsearch/get',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

post_url = 'http://www.ceigle.com/epsearch/getlist'

data = {
    'key': '德邦',
    'pageno': 100
}

response = requests.post(url=post_url, data=data, headers=headers)
print(response.text.replace('<em>', '').replace('</em>', ''))
'''
{"total":"28021","pageno":100,"totalPage":"100",
"list":[{"openStatus":"开业","entName":"深圳市鑫德邦科技有限公司","entLogo":"","pid":"31990482768758","validityFrom":"2014-08-27","titleDomicile":"深圳市宝安区航城街道黄麻布社区勒竹角鸿竹雍啟科技园D栋综合楼七楼A单元","logoWord":"鑫德邦","tags":[],"labels":{"executed":{"style":"red","text":"被执行人"},"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司","hitReason":[{"企业名称":"深圳市鑫德邦科技有限公司"}],"titleName":"深圳市鑫德邦科技有限公司","legalPerson":"吕玉梅","scope":"一般经营项目是：电子产品、五金制品、防护用品、二类医疗器械、照明产品、数码产品的研发与销售；国内贸易，货物及技术进出口。，许可经营项目是：电子产品的生产、加工。","domicile":"深圳市宝安区航城街道黄麻布社区勒竹角鸿竹雍啟科技园D栋综合楼七楼A单元","regCap":"50.0万","titleLegal":"吕玉梅","bid":"310482768758"},{"openStatus":"开业","entName":"黑龙江德邦物业管理有限公司","entLogo":"","pid":"11330067255603","validityFrom":"2019-01-18","titleDomicile":"哈尔滨市香坊区木材东街25-1号明光水岸小区1单元12层3号(住宅)","logoWord":"德邦物业","tags":[],"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人投资或控股)","hitReason":[{"企业名称":"黑龙江德邦物业管理有限公司"}],"titleName":"黑龙江德邦物业管理有限公司","legalPerson":"张林江","scope":"物业管理，物业服务，环境卫生管理服务，房地产经纪服务（不含典当及拍卖），室内外装饰装修工程，上下水管道维修、疏通，防水工程，保温工程，保洁服务，综合贸易市场管理服务，市场摊位出租，城市停车场服务，企业管理咨询服务，园林绿化工程施工，城市亮化工程施工，房屋建筑工程施工，水利水电工程施工，钢结构工程施工，环保工程施工，公路工程施工，土石方工程施工，地基与基础工程施工，水电安装工程施工，电气工程施工，消防工程施工，安防工程施工，结构加固工程施工，建筑幕墙工程施工，市政公用工程施工，建筑智能化工程施工；批发兼零售：蔬菜、水果、粮食、生鲜肉、水产品、禽类、蛋类、农副产品、土特产品、山特产品、日用品、办公用品、五金交电、机电设备、监控设备、水暖建材、劳保用品、机械设备配件、汽车配件；管道工程，消防器材、消防设施现场安装、维修、保养，汽车租赁服务，自有房屋租赁，货物运输代理服务，普通冷库服务，搬运装卸服务。","domicile":"哈尔滨市香坊区木材东街25-1号明光水岸小区1单元12层3号(住宅)","regCap":"100.0万","titleLegal":"张林江","bid":"113307255603"},{"openStatus":"开业","entName":"沈阳德邦医疗器械有限公司","entLogo":"","levelAtaxer":[2016],"pid":"31064187173914","validityFrom":"2012-06-06","titleDomicile":"辽宁省沈阳市于洪区沙岭路2-1号（2218门）","logoWord":"德邦医疗","tags":{"laTaxer":"<span class=\"zx-ent-tag laTaxer\">A级纳税人(2016)</span>"},"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人投资或控股)","hitReason":[{"企业名称":"沈阳德邦医疗器械有限公司"}],"titleName":"沈阳德邦医疗器械有限公司","legalPerson":"杨军红","scope":"许可经营项目：三类：注射穿刺器械、医用电子仪器设备、医用激光仪器设备、医用高频仪器设备、植入材料和人工器官、医用高分子材料及制品零售；二类：神经外科手术器械零售； 一般经营项目：无（依法须经批准的项目，经相关部门批准后方可开展经营活动。）","domicile":"辽宁省沈阳市于洪区沙岭路2-1号（2218门）","regCap":"120.0万","titleLegal":"杨军红","bid":"310641873914"},{"openStatus":"开业","entName":"深圳市德邦物业管理有限公司","entLogo":"","pid":"31845317702613","validityFrom":"2011-07-14","titleDomicile":"深圳市龙岗区布吉街道东门头国都花园商住楼天茂阁11F号","logoWord":"德邦物业","tags":[],"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人独资)","hitReason":[{"企业名称":"深圳市德邦物业管理有限公司"}],"titleName":"深圳市德邦物业管理有限公司","legalPerson":"陈晓健","scope":"一般经营项目是：物业管理；五金、建材的购销（不含再生资源回收经营）；国内贸易（法律、行政法规、国务院决定规定在登记前须经批准的项目除外）；货物进出口、技术进出口（法律、行政法规禁止的项目除外；法律、行政法规限制的项目须取得许可后方可经营）。，许可经营项目是：","domicile":"深圳市龙岗区布吉街道东门头国都花园商住楼天茂阁11F号","regCap":"100.0万","titleLegal":"陈晓健","bid":"318453102613"},{"openStatus":"开业","entName":"方正县德邦货物运输有限公司","entLogo":"","pid":"31435982369458","validityFrom":"2017-09-05","titleDomicile":"方正县方正县前进街爱建小区六号楼厢房一层南数第二屋","logoWord":"德邦货物","tags":[],"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人投资或控股)","hitReason":[{"企业名称":"方正县德邦货物运输有限公司"}],"titleName":"方正县德邦货物运输有限公司","legalPerson":"王金龙","scope":"道路普通货物运输（不含易燃易爆及危险化学物品）；普通货物仓储（不含易燃易爆及危险化学物品）；货物物流信息咨询服务（不含商业秘密）；货场内的货物装卸服务（不含易燃易爆及危险化学物品）。","domicile":"方正县方正县前进街爱建小区六号楼厢房一层南数第二屋","regCap":"200.0万","titleLegal":"王金龙","bid":"315982369458"},{"openStatus":"开业","entName":"松潘县德邦物流有限责任公司","entLogo":"","pid":"59002342921699","validityFrom":"2014-01-03","titleDomicile":"松潘县进安乡顺城南路","logoWord":"德邦物流","tags":[],"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人独资)","hitReason":[{"企业名称":"松潘县德邦物流有限责任公司"}],"titleName":"松潘县德邦物流有限责任公司","legalPerson":"汪孝东","scope":"普通货物运输。（依法须经批准的项目，经相关部门批准后方可开展经营活动）","domicile":"松潘县进安乡顺城南路","regCap":"120.0万","titleLegal":"汪孝东","bid":"590022921699"},{"openStatus":"开业","entName":"芜湖德邦文化传媒有限公司","entLogo":"","pid":"71661623039554","validityFrom":"2012-11-20","titleDomicile":"芜湖市镜湖区名流SOHO922","logoWord":"德邦文化","tags":{"abnormal":"<span class=\"zx-ent-tag abnormal\">经营异常</span>"},"labels":{"abnormal":{"style":"red","text":"经营异常"},"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人投资或控股)","hitReason":[{"企业名称":"芜湖德邦文化传媒有限公司"}],"titleName":"芜湖德邦文化传媒有限公司","legalPerson":"蒋志亮","scope":"婚庆礼仪、开业庆典服务，广告策划、发布、制作，图文设计，标牌制作。","domicile":"芜湖市镜湖区名流SOHO922","regCap":"50.0万","titleLegal":"蒋志亮","bid":"711623039554"},{"openStatus":"开业","entName":"湖北德邦物业服务有限公司","entLogo":"","pid":"37200472905417","validityFrom":"2012-06-25","titleDomicile":"城站路","logoWord":"德邦物业","tags":[],"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人独资)","hitReason":[{"企业名称":"湖北德邦物业服务有限公司"}],"titleName":"湖北德邦物业服务有限公司","legalPerson":"褚砚华","scope":"凭资质证书从事物业服务、房屋中介服务；家政服务；五金、建筑材料（不含钢材及木材）销售。 （涉及许可经营项目，应取得相关部门许可后方可经营）","domicile":"城站路","regCap":"300.0万","titleLegal":"褚砚华","bid":"300472905417"},{"openStatus":"开业","entName":"怀远县德邦建筑工程有限公司","entLogo":"","pid":"30304921653908","validityFrom":"2020-03-18","titleDomicile":"安徽省蚌埠市怀远县榴城镇壹号院小区46号楼102号商铺","logoWord":"德邦建筑","tags":[],"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司(自然人独资)","hitReason":[{"企业名称":"怀远县德邦建筑工程有限公司"}],"titleName":"怀远县德邦建筑工程有限公司","legalPerson":"崔苏雅","scope":"地基基础工程、园林绿化工程、水利工程、市政工程、建筑工程施工；建筑材料销售；工程机械设备安装、租赁服务；货物装卸搬运服务。（依法须经批准的项目，经相关部门批准后方可开展经营活动）","domicile":"安徽省蚌埠市怀远县榴城镇壹号院小区46号楼102号商铺","regCap":"50.0万","titleLegal":"崔苏雅","bid":"304921653908"},{"openStatus":"开业","entName":"利津县德邦化工有限责任公司","entLogo":"","pid":"30797249101225","validityFrom":"2000-12-06","titleDomicile":"利津县城津一路208号","logoWord":"德邦化工","tags":[],"labels":{"opening":{"style":"blue","text":"开业"}},"entType":"有限责任公司","hitReason":[{"企业名称":"利津县德邦化工有限责任公司"}],"titleName":"利津县德邦化工有限责任公司","legalPerson":"赵利民","scope":"蜡油、渣油销售（国家限制、禁止经营的除外，需凭审批和许可经营的凭审批文件和许可证经营）。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。","domicile":"利津县城津一路208号","regCap":"58.0万","titleLegal":"赵利民","bid":"307972491225"}]}

http://www.ceigle.com/epsearch/compinfo?pid=31990482768758

详情页使用pid字段拼接

'''
