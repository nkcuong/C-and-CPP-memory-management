import threading
import time
import random

DUNG_LUONG = 100

class HangDoiSanXuatTieuThu:
	def __init__(self):
		self.data = [None] * DUNG_LUONG
		self.front = self.rear = -1
		self.mutex = threading.Lock()
		self.not_empty = threading.Condition(self.mutex)

def khoi_tao_hang_doi():
	return HangDoiSanXuatTieuThu()

def san_xuat(hang_doi, mat_hang):
	with hang_doi.mutex:
		while (hang_doi.rear + 1) % DUNG_LUONG == hang_doi.front:
			hang_doi.not_empty.wait()
	if hang_doi.front == -1:
		hang_doi.front = 0
		hang_doi.rear = 0
	else:
		hang_doi.rear = (hang_doi.rear + 1) % DUNG_LUONG

	hang_doi.data[hang_doi.rear] = mat_hang
	hang_doi.not_empty.notify()

def tieu_thu(hang_doi):
	with hang_doi.mutex:
		while hang_doi.front == -1:
			hang_doi.not_empty.wait()

		mat_hang = hang_doi.data[hang_doi.front]

		if hang_doi.front == hang_doi.rear:
			hang_doi.front = -1
			hang_doi.rear = -1
		else:
			hang_doi.front = (hang_doi.front + 1) % DUNG_LUONG

		hang_doi.not_empty.notify()

	return mat_hang

def luong_san_xuat(nha_san_xuat):
	while nha_san_xuat['dem'] < nha_san_xuat['dung_luong']:
		time.sleep(nha_san_xuat['toc_do'])
		i = random.randint(1, 1000)
		san_xuat(nha_san_xuat['hdstt'], i)
		nha_san_xuat['vuaSanXuat'] = i
		print(f"Nha san xuat {nha_san_xuat['name']} vua san xuat: {i} - hang doi: {((nha_san_xuat['hdstt'].rear - nha_san_xuat['hdstt'].front + DUNG_LUONG) % DUNG_LUONG) + 1}")
		nha_san_xuat['dem'] += 1

def luong_tieu_thu(nguoi_tieu_thu):
	while nguoi_tieu_thu['dem'] < nguoi_tieu_thu['dung_luong']:
		time.sleep(nguoi_tieu_thu['toc_do'])
		i = tieu_thu(nguoi_tieu_thu['hdstt'])
		nguoi_tieu_thu['vuaTieuThu'] = i
		if i != -1:
			print(f"Nguoi tieu thu {nguoi_tieu_thu['name']} vua tieu thu: {i} - hang doi: {((nguoi_tieu_thu['hdstt'].rear - nguoi_tieu_thu['hdstt'].front + DUNG_LUONG) % DUNG_LUONG) + 1}")
		nguoi_tieu_thu['dem'] += 1

def main():
	n = int(input("Nhap dung luong: "))

	hdstt = khoi_tao_hang_doi()

	luong_nha_san_xuat = []
	luong_nguoi_tieu_thu = []

	nha_san_xuat = [{'name': str(i + 1), 'hdstt': hdstt, 'dung_luong': 100, 'dem': 0, 'toc_do': 2, 'vuaSanXuat': -1} for i in range(4)]
	nguoi_tieu_thu = [{'name': str(i + 1), 'hdstt': hdstt, 'dung_luong': 100, 'dem': 0, 'toc_do': 1.5, 'vuaTieuThu': -1} for i in range(2)]

	for nha_san_xuat in nha_san_xuat:
		thread = threading.Thread(target=luong_san_xuat, args=(nha_san_xuat,))
		luong_nha_san_xuat.append(thread)
		thread.start()

	time.sleep(2)

	for nguoi_tieu_thu in nguoi_tieu_thu:
		thread = threading.Thread(target=luong_tieu_thu, args=(nguoi_tieu_thu,))
		luong_nguoi_tieu_thu.append(thread)
		thread.start()

	for thread in luong_nha_san_xuat:
		thread.join()

	for thread in luong_nguoi_tieu_thu:
		thread.join()

if __name__ == "__main__":
	main()