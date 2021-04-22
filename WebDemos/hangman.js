var haslo = 'Man programming is so cool';
haslo = haslo.toUpperCase();
var enchaslo='';
var len=haslo.length;
var skuchy = 0;
var yessnd = new Audio('https://www.github.com/JakubKwantowy/KwantowyGames-Team/raw/Master/WebDemos/hangman/yes.wav');
var nosnd = new Audio('https://www.github.com/JakubKwantowy/KwantowyGames-Team/raw/Master/WebDemos/hangman/no.wav');

for(i=0;i<len;i++){
	if(haslo.charAt(i)==' ') enchaslo = enchaslo+' '; 
	else enchaslo = enchaslo+'-'; 
}

function wypisz_haslo(){
	document.getElementById('plansza').innerHTML = enchaslo;
}

function custom(){
	enchaslo = '';
	haslo = document.getElementById('ctext').value;
	haslo = haslo.toUpperCase();
	var len=haslo.length;
	for(i=0;i<len;i++){
	if(haslo.charAt(i)==' ') enchaslo = enchaslo+' '; 
	else enchaslo = enchaslo+'-'; 
}
	start();
	
}

var litery = new Array(26);

litery[0] = 'A';
litery[1] = 'B';
litery[2] = 'C';
litery[3] = 'D';
litery[4] = 'E';
litery[5] = 'F';
litery[6] = 'G';
litery[7] = 'H';
litery[8] = 'I';
litery[9] = 'J';
litery[10] = 'K';
litery[11] = 'L';
litery[12] = 'M';
litery[13] = 'N';
litery[14] = 'O';
litery[15] = 'P';
litery[16] = 'Q';
litery[17] = 'R';
litery[18] = 'S';
litery[19] = 'T';
litery[20] = 'U';
litery[21] = 'V';
litery[22] = 'W';
litery[23] = 'X';
litery[24] = 'Y';
litery[25] = 'Z';


//window.onload=start;

function start(){
	//setup stuff
	var div = '';
	for(i=0; i<26; i++){
		//document.getElementById('alfabet').innerHTML = 'dgdgdg';
		div=div + '<div onclick="test('+i+');" id="lit'+i+'" class="litera">'+litery[i]+'</div>';
		if((i+1) % 6 == 0) div=div + '<div style="clear:both;"></div>';
	}
	
	document.getElementById('alfabet').innerHTML = div;
	
	//write password
	wypisz_haslo();
}

String.prototype.setChar = function(pos, char){
	if(pos > this.length - 1){return this.toString();}
	else return this.substr(0, pos) + char + this.substr(pos+1);
}

function test(nr){
	var trafiona = false;
	//alert(litery[nr]);
	for(i=0; i<len; i++){
		if(haslo.charAt(i) == litery[nr]){
			//alert(i)
			enchaslo=enchaslo.setChar(i,litery[nr]);
			trafiona = true;
		}
	}
	if(trafiona == true){
		yessnd.play();
		var element = 'lit'+nr;
		document.getElementById(element).style.background = '#003300';
		document.getElementById(element).style.color = '#00C000';
		document.getElementById(element).style.border = '3px solid #00C000';
		document.getElementById(element).style.cursor = 'default';
	   
	   wypisz_haslo()
	}else{
		nosnd.play();
		var element = 'lit'+nr;
		document.getElementById(element).style.background = '#330000';
		document.getElementById(element).style.color = '#C00000';
		document.getElementById(element).style.border = '3px solid #C00000';
		document.getElementById(element).style.cursor = 'default';
		document.getElementById(element).setAttribute('onclick','alert("stop!");');
		
		//skucha
		skuchy++;
		var obraz = 'https://raw.githubusercontent.com/JakubKwantowy/KwantowyGames-Team/Master/WebDemos/hangman/s'+skuchy+'.jpg';
		document.getElementById('szubienica').innerHTML = '<img src="'+obraz+'" title="error: '+skuchy+'"/>';
	}
	
	//wygrana
	if(haslo == enchaslo){
	   document.getElementById('alfabet').innerHTML = 'You won!!! <br/><br/> <span class="reset" onclick="location.reload();">Wanna retry?</span>';
	}
	
	if(skuchy >= 9){
	   document.getElementById('alfabet').innerHTML = 'You Lost. <br/><br/> <span class="reset" onclick="location.reload();">Wanna retry?</span>';
	}
}
