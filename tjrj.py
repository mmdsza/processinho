import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from captcha_solver import CaptchaSolver
class tjrj:
	def find(self, processo):
		source = 'http://www.tjrj.jus.br/'
		driver = webdriver.Chrome()
		driver.get(source)
		numinput = '//*[@id="parte1ProcCNJ"]'
		findprocess = '//*[@id="form:commandButton3"]'
		driver.find_element_by_xpath(numinput).send_keys(processo)
		driver.find_element_by_xpath(findprocess).click()
	def content():
		link = driver.get(driver.current_url)
		html = driver.page_source
		page_soup = soup(html, 'html.parser')
		advogados = page_soup.find_all("table", {"class":"info"})
		return advogados

processo = '00714592120150038'
a = tjrj()
getProcesso = a.find(processo)
getcontent = getProcesso.content()