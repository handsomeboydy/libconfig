# Defined in - @ line 1
function sps --description 'alias sps sudo pacman -S'
	sudo pacman -S $argv;
end
