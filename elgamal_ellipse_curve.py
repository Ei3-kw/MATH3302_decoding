import string
import fibonacci_lfsr

if __name__ == '__main__':
	text = 'Blink'
	for c in text:
		print(fibonacci_lfsr.char2index(c))