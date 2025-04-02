all: guesses.txt answers.txt

guesses.txt:
	curl https://gist.githubusercontent.com/cfreshman/40608e78e83eb4e1d60b285eb7e9732f/raw/9a798fdcb05a6797578d13b4b9e0c62e9db9aacb/wordle-nyt-allowed-guesses.txt -o guesses.txt

answers.txt:
	curl https://gist.githubusercontent.com/cfreshman/a7b776506c73284511034e63af1017ee/raw/60531ab531c4db602dacaa4f6c0ebf2590b123da/wordle-nyt-answers-alphabetical.txt -o answers.txt
