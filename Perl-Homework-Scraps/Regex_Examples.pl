#Scott Efird
#Lab 11
#COSC 4750

#REMEMBER, e-mail me with the subject COSC4750: Lab <#>

$filename = $ARGV[0];
open(fh, $filename)
	or die "Could not open file '$filename' $!"; 
@arrayOfLines = <fh>;

foreach $Line (@arrayOfLines){
	chomp($Line);
	print "$Line \n";
	
	#If there is no period in the line, then print 1
	if($Line !~ /\./g){
		print "1 ";
	}
		
	#If after a comma, the word one is on the line, then print 2
	if($Line =~ /,.+(one)/){
		print "2 ";
	}
	
	#If there are only 7 words on the line, print 3	
	$count = $Line =~ s/((^|\s)\S)/$1/g;
	if($count eq 7){
		print "3 ";
	}
	
	#f there is a number (like 1, 2, etc), print 4
	if ($Line =~ /[0-9]/){
		print "4 ";
	}
	
	#If the letters a, b, and c (any case) come in alpabetical order, not counting non-letters, like spaces, numbers, etc.
	#example: a.2b -.C is correct. But abdc is not correct. Print 5
	
	if($Line =~ /a\Wb\Wc\W/i){
		print "5 ";
	}
	
	#If there are at least 6 lowercase e's on a line, print 6
	$count = $Line =~ s/((^|\w*)e\w*)/$1/g;		
	if($count >= 6){
		print "6 ";
	}
	
	#If the following letters appear in order on a line, anything else between them doesn't matter. 
	#w a s g m then print 7
	if($Line =~ /w.*a.*s.*g.*m/){
		print "7 ";	
	}
	
	
	#Like number 7, except the letters p r i n t appear in order. print 8
	if($Line =~ /p.*r.*i.*n.*t/){
		print "8 ";
	}
	
	#At the start of a line there is a th, followed somewhere on the line with a capital I, then somewhere after that a semicolon ; print 9
	if($Line =~ /th.*I.*\;/){
		print "9 ";
	}
	
	#The start of a line has either a t or o, followed somewhere in the line by another t, and the last character in the line must be an a, e, i, o, or u. This is also case insensitive. Print a 10
	if($Line =~ /t(t|o).*t.*(a|e|i|o|u)+\s/i){
		print "10 ";
	}
	print "\n";
}
