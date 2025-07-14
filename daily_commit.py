
import os
from datetime import datetime

def daily_commit():
    # Get the current date
    today = datetime.now().strftime('%Y-%m-%d')
    file_name = f'{today}.txt'

    # Create a new file with the current date as the filename
    with open(file_name, 'w') as f:
        f.write(f'Commit for {today}')

    # Git commands
    os.system('git add .')
    os.system(f'git commit -m "Daily commit for {today}"')

if __name__ == '__main__':
    daily_commit()
