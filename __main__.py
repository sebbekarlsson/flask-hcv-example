from example.app import app
import subprocess


if __name__ == '__main__':
    subprocess.Popen(
        ['/usr/local/bin/hcv', "640", '480', 'http://localhost:5000', '1'])
    app.run()
