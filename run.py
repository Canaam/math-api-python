# -*- coding: utf-8 -*-

from app.app import app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)