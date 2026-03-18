.PHONY: create-practice remove-practice

create-practice:
	mkdir -p $(NAME)
	cp PracticeMakefile $(NAME)/Makefile

remove-practice:
	rm -rf $(NAME)
