import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Login'))

from Login.login import ModernLogin

if __name__ == "__main__":
    ModernLogin()