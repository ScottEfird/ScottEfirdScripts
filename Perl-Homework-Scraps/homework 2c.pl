#Scott Efird
#Homework #5
#COSC 4750
#Exercise 6
#Reads a name, num, num, num. 
#Prints to a fancy formatting thing.
#Note, this code does not run correctly, I wasn't able to figure out how to pull the info from
#the array without getting an error. The code here in my mind should be right but does not run. 
$filename = $ARGV[0];
open(fh, $filename)
	or die "Could not open file '$filename' $!"; 
@array = <fh>;
chomp (@array);


format STDOUT_TOP =
				Name			Score1	Score2	Score 3	Score4
				-----------------------------------------------
				.
		
for my $row (@arr) {
format STDOUT =
				@<<<<<<<<<<<<  @<<  @<<  @<<  @<<
				@{$row}, {$num1},{$num2},{$num3},{$num4};
				.
				foreach $revLine (@array){					
				write;
				}
}
