#Scott Efird
#Homework #5
#COSC 4750
#Exercise 5
#Read a list of numbers from a file, add up all the values
#Print the sum followed by a sorted list of numbers.
$filename = $ARGV[0];
open(fh, $filename)
	or die "Could not open file '$filename' $!"; 
@arrayOfGrades = <fh>;
chomp (@arrayOfGrades);
foreach $revLine (@arrayOfGrades){
	$Sum = $Sum + $revLine;	
}
@arrayOfGrades = sort {$b <=> $a} @arrayOfGrades;
print "The sum of the numbers is $Sum \n";
foreach $revLine (@arrayOfGrades){
	print "$revLine \n";
}