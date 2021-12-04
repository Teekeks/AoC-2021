from typing import List
import requests


def get_input(day) -> List[str]:
    with open('session.txt', 'r') as f:
        ses = {'session': f.read()}
        return requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=ses).text.splitlines()
