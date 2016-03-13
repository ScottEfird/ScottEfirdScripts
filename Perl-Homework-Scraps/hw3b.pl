#Scott Efird
#Homework #7
#COSC 4750
#Exercise 12
#Use grading program, make it run as a function.
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










#Exercise 13
use Socket;
use IO::Handle;
$remote_host = "hive1.cs.uwyo.edu";
$remote_port = 3012;
socket(SERVER, PF_INET, SOCK_STREAM, getprotobyname('tcp'));
SERVER->autoflush(1); #socket doesn't have autoflush turned on.
$internet_addr = inet_aton($remote_host) or die "Can't convert $!\n";
 
$paddr = sockaddr_in($remote_port, $internet_addr);
connect (SERVER, $paddr)  or die "can't connect $!\n";
print SERVER "connection from Scott \n";
$answer = <SERVER>;
close SERVER;
{
	print "$answer \n";
}
#Exercise 14
use IO::Socket;
$server_port = 3012;
$server = IO::Socket::INET->new (LocalPort => $server_port, Type => SOCK_STREAM, Reuse=> 1, Listen => SOMAXCONN)
    or die "Failed to open port $server_port: $@\n";
$client = $server->accept(); 
$line = <$client>;
print "Connection from $line \n";
print CLIENT "Hi $line \n";
close $client; 
close $server;













