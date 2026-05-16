from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. 현재 날짜 구하기 (서버 시간 기준)
        current_date_str = datetime.now().strftime("%Y%m%d")
        current_date_num = int(current_date_str)
        
        # 2. 알고리즘 적용 (솔트, 매직 넘버는 서버 내부에만 존재)
        MY_SALT = 773
        MAGIC_NUMBER = 1234
        calculated_value = (current_date_num * MY_SALT) + MAGIC_NUMBER
        
        # 3. 뒤에서 6자리 추출
        daily_password = str(calculated_value)[-6:]
        
        # 4. 응답 헤더 및 바디 작성 (JSON 형태로 전달)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # CORS 허용 (정적 페이지에서 API를 호출할 수 있도록)
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        
        response_data = {"password": daily_password}
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        return