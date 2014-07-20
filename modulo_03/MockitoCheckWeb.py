from mockito import mock, when, verify
import unittest

class CheckWeb:
	def check(self, web, server, log):
		result = server.connect(web)
		if result.isOk():
			log.webIsOk(web)
		else:
			log.webIsWrong(web, result)

class TestCheckWeb(unittest.TestCase):
	def test_webIsOk(self):
		cw = CheckWeb()
		web = mock()
		server = mock()
		log = mock()
		result = mock()

		when(server).connect(web).thenReturn(result)
		when(result).isOk().thenReturn(True)
		when(log).webIsOk(web).thenReturn(None)

		cw.check(web, server, log)

		verify(server).connect(web)
		verify(result).isOk()
		verify(log).webIsOk(web) 

	def test_webIsWrong(self):
		cw = CheckWeb()
		web = mock()
		server = mock()
		log = mock()
		result = mock()

		when(server).connect(web).thenReturn(result)
		when(result).isOk().thenReturn(False)
		when(log).webIsWrong(web, result).thenReturn(None)

		cw.check(web, server, log)

		verify(server).connect(web)
		verify(result).isOk()
		verify(log).webIsWrong(web, result) 



# Main
if __name__ == '__main__':
    unittest.main()