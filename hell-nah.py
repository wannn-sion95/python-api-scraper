import requests
import xlwt
from xlwt import Workbook

BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',
}


def get_jobs_postings():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    if res.status_code == 200:
        return res.json()
    else:
        print(f"Permintaan gagal dengan status: {res.status_code}")
        return []


def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    
    # Tuliskan header
    headers = list(data[0].keys())
    for i in range(len(headers)):
        job_sheet.write(0, i, headers[i])  # Baris header

    # Tuliskan data
    for i in range(len(data)):
        job = data[i]
        values = list(job.values())
        for x in range(len(values)):
            job_sheet.write(i + 1, x, str(values[x]))  # Baris data mulai dari 1

    wb.save('remoteok_jobs.xls')
    print("Data berhasil disimpan ke remoteok_jobs.xls")


if __name__ == "__main__":
    json = get_jobs_postings()
    if isinstance(json, list) and len(json) > 1:
        json = json[1:]  # Abaikan elemen pertama
        output_jobs_to_xls(json)
    else:
        print("Data JSON tidak valid atau kosong.")
