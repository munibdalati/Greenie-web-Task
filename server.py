from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import psutil
import time

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/calculate_power'):
            query_components = parse_qs(urlparse(self.path).query)
            app_name = query_components["app"][0]
            duration = int(query_components["duration"][0])

            power_consumption = self.get_process_power_consumption(app_name, duration)
            if power_consumption is None:
                response = f"There is no {app_name} application in your computer"
            else:
                response = f"Estimated power consumption of {app_name} is {round(power_consumption,1)} % of CPU capacity"


            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())

    def get_process_power_consumption(self, process_name, duration_seconds):
        process_name_lower = process_name.lower()
        # Find the process by name
        target_process = None
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'].lower() == process_name_lower:
                target_process = psutil.Process(process.info['pid'])
                break

        if not target_process:
            return None

        # Get initial process CPU usage
        initial_cpu_usage = psutil.cpu_percent(1)

        # Sleep for the 1 second
        time.sleep(1)

        # Get final process CPU usage
        final_cpu_usage = psutil.cpu_percent(1)

        # Calculate average CPU usage over the duration
        average_cpu_usage = (initial_cpu_usage + final_cpu_usage) / 2

        # Assuming a rough correlation between CPU usage and power consumption
        estimated_power_consumption = average_cpu_usage * duration_seconds
        print(estimated_power_consumption)
        return estimated_power_consumption


# Running the server by writing "python server.py" in the terminal
if __name__ == '__main__':
    PORT = 8000  # Define the port
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Server is running at http://localhost:{PORT}')
    httpd.serve_forever()

