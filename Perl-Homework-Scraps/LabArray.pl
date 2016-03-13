#Problem 1
$filename = $ARGV[0];
open(fh, $filename)
	or die "Could not open file '$filename' $!"; 
@lines = <fh>;
@rev = reverse(@lines);
foreach $revLine (@rev){
	print $revLine;
}

#Problem 2
%friends_ages = ("Allen", 23,
                 "Lisa", 19,
                 "Alice", 29,
                 "Spot", "28 in dog years",
                 "Bob", 22);
				 
print  "Enter 1 for print in any order
Enter 2 for print by ordered name
Enter 3 for print by ordered age
Enter -1 to quit \n";

while($sentinel == false){
	$check = <STDIN>;
	#Quits
	if($check == -1){
		$sentinel = true;
		exit;		
	}
	#Prints out the hashArray
	if($check == 1){
		print "\n";
		while (my ($k,$v)=each %friends_ages){print "$k $v\n"};
		print "\n";
		}
	#Sorts hashArray by name, then prints
	if($check ==2){
	print "\n";
	foreach my $name (sort {lc $a cmp lc $b} keys %friends_ages){
		printf "%-10s %s\n", $name, $friends_ages{$name};
		}
	print "\n";
	}
	#Sorts hashArray by age, then prints
	if($check ==3){
		print "\n";
		foreach my $name (sort { $friends_ages{$a} <=> $friends_ages{$b} } keys %friends_ages) {
		printf "%-10s %s\n", $name, $friends_ages{$name};
		}
	print "\n";
	}
}
