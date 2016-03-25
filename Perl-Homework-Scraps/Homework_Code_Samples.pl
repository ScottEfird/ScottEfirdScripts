#Scott Efird
#Homework #4
#COSC 4750


#Exercise 1
#Write a script that reads in a temperature in 
#Fahrenheit and prints out the equivalent temperature in Celsius
print "Please enter a temperature in Fahrenheit: \n";
$number1 = <STDIN>;
chomp($number1);
$number1 = ($number1 - 32) * (5/9);
print $number1;



#Exercise 2
#Write a perl script that reads numbers between 0 and 100.
#It will stop reading if it hits a sentinel value of -1.
#It will print out the number and grade it.
use Switch;
print "Please enter a number to be graded, -1 to stop: \n";
$sentinel = false;
while($sentinel == false){
	$grade = <STDIN>;
	if($grade == -1){
		$sentinel = true;
		exit loop;		
	}	
	switch ($grade) {
			case [90..100] 		{print "Your grade is a A \n"};
			case [80..89] 		{print "Your grade is a B \n"};
			case [70..79] 		{print "Your grade is a C \n"};
			case [60..69] 		{print "Your grade is a D \n"};
			case [0..59] 		{print "Your grade is a F \n"};
	}
}

#Scott Efird
#Homework #5
#COSC 4750
#Exercise 3 and 4
#Write a perl script that reads numbers from a file and grade them.
#Print out min/max/avg
use Switch;
$filename = $ARGV[0];
open(fh, $filename)
	or die "Could not open file '$filename' $!"; 
@arrayOfGrades = <fh>;
$Min = 100;
$Max = 0;

#Grade Function definition
sub grade{
	#Adding the value to the total sum of grade scores.
	$GradeSum = $GradeSum + $revLine;
	$Count = $Count + 1;
	#Checking for max
	if($revLine > $Max){
		$Max = $revLine;
	}
	#Checking for min
	if($revLine < $Min){
		$Min = $revLine;
	}
	#Grading the score from the file line
	switch ($revLine) {
			case [90..100] 		{print "Your score is $revLine , Your grade is a A \n"};
			case [80..89] 		{print "Your score is $revLine , Your grade is a B \n"};
			case [70..79] 		{print "Your score is $revLine , Your grade is a C \n"};
			case [60..69] 		{print "Your score is $revLine , Your grade is a D \n"};
			case [0..59] 		{print "Your score is $revLine , Your grade is a F \n"};
	}
}


foreach $revLine (@arrayOfGrades){
	grade(chomp($revLine));
}
print "---------------------------------------- \n";
print "The highest score was $Max and the lowest score was $Min \n";
$avg = ($GradeSum/$Count);
print "The average of the scores was $avg";