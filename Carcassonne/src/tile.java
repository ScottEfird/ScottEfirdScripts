public class tile {
	public String Name; //Might not need, just file name? 
	public double X_Location;
	public double Y_Location;
	
	//Each game tile has four faces, UP, DOWN, LEFT, RGHT
	//Each side of the tile can only match one type (Grass, City, Road)
	
	
	//Constructor
	public tile(String Name, double X_Location, double Y_Location){
		Name = null;
		X_Location = -1;
		Y_Location = -1;
	}
	
	/**
	 * Returns the X location of the tile in the form of a double. 
	 */
	public double get_X_Location(){
		return X_Location;
	}
	
	/**
	 * Returns the Y location of the tile in the form of a double. 
	 */
	public double get_Y_Location(){
		return Y_Location;
	}
	
}
