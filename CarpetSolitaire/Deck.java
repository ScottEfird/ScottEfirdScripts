import java.awt.Point;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Deck {	
	//Data Members
	//
	//Single suits for checking valid moves. 
	public String[] Clubs = {"aceClubs", "twoClubs", "threeClubs", "fourClubs", "fiveClubs", "sixClubs", "sevenClubs", "eightClubs", "nineClubs", "tenClubs", "jackClubs", "queenClubs","kingClubs"}; 
	public String[] Diamonds = { "aceDiamonds", "twoDiamonds", "threeDiamonds", "fourDiamonds", "fiveDiamonds", "sixDiamonds", "sevenDiamonds", "eightDiamonds", "nineDiamonds", "tenDiamonds", "jackDiamonds", "queenDiamonds","kingDiamonds"};
	public String[] Hearts = { "aceHearts", "twoHearts", "threeHearts", "fourHearts", "fiveHearts", "sixHearts", "sevenHearts", "eightHearts", "nineHearts", "tenHearts", "jackHearts", "queenHearts","kingHearts"};
	public String[] Spades = { "aceSpades", "twoSpades", "threeSpades", "fourSpades", "fiveSpades", "sixSpades", "sevenSpades", "eightSpades", "nineSpades", "tenSpades", "jackSpades", "queenSpades","kingSpades"};
	
	public String[] CardDeck = {"aceClubs", "twoClubs", "threeClubs", "fourClubs", "fiveClubs", "sixClubs", "sevenClubs", "eightClubs", "nineClubs", "tenClubs", "jackClubs", "queenClubs","kingClubs",
								"aceDiamonds", "twoDiamonds", "threeDiamonds", "fourDiamonds", "fiveDiamonds", "sixDiamonds", "sevenDiamonds", "eightDiamonds", "nineDiamonds", "tenDiamonds", "jackDiamonds", "queenDiamonds","kingDiamonds",
								"aceHearts", "twoHearts", "threeHearts", "fourHearts", "fiveHearts", "sixHearts", "sevenHearts", "eightHearts", "nineHearts", "tenHearts", "jackHearts", "queenHearts","kingHearts",
								"aceSpades", "twoSpades", "threeSpades", "fourSpades", "fiveSpades", "sixSpades", "sevenSpades", "eightSpades", "nineSpades", "tenSpades", "jackSpades", "queenSpades","kingSpades"};
	
	public int deckSize = 52;
	public Map<String, Point> DeckMap = new HashMap<String, Point>();	
	public Map<String, Point> CardLocations = new HashMap<String, Point>();	
	
	Deck()
	{
		Point defultPoint = new Point(-999, -999);
		

		for(int i = 0; i != deckSize; i++)
		{
			DeckMap.put(CardDeck[i],defultPoint);
		}	
	}
	
	/**
	 * Get the size of the deck
	 */
	public int getDeckSize()
	{
		return deckSize;
	}
	
	/**
	 * Prints the whole deck as a string.
	 */
	public void printFullArray()
	{
		System.out.println(Arrays.toString(CardDeck));
	}	
	
	/**
	 * Give the map a key, returns the value at the key.
	 */
	public Point getDeckMap(String Key)
	{
		return DeckMap.get(Key);
	}
	
	/**
	 * Looks at DeckMap, if there is something at the given point 
	 * Lookforkey returns the key, else it returns "none".
	 * 
	 * 
	 * If there is a card, you get just get your point back, else you get a none.
	 */
	public String lookForKey(Point value)
	{
        for (Entry<String, Point> entry : DeckMap.entrySet()) {
            if (entry.getValue().equals(value)) {
                //System.out.println(entry.getKey());                
                return entry.getKey();
            }
        }
		return "none";
	}
	
	
	/**
	 * Set the value at the key to a new value.
	 */
	public void setDeckMap(String Key, Point value)
	{
		DeckMap.put(Key,value);
		
	}	
		
	/**
	 * Returns the deck
	 */
	public String[] getDeck()
	{
		return CardDeck;		
	}
	
	
	/**
	 * returns the CardLocations map
	 */
	public Map<String, Point> getCardLocations()
	{
		return CardLocations;
	}
	
	/**
	 * Adds a location to the CardLocations
	 */
	public void setDefaultLocation(int X, int Y, int i)
	{
		Point position = new Point(X,Y);		
		CardLocations.put(Integer.toString(i),position);
	}
	
	
	
	/**
	 * Give it a location, it will return the normal default card location point for snapping.
	 */
	public Point getDefaultPoint(int location)
	{
		return CardLocations.get(Integer.toString(location));
	}
	
	/**
	 * Grabs  a card at int location in the deck, returns the name of card stored there.
	 */
	public String getCard(int location)
	{
		return CardDeck[location];
	}
	
	/**
	 * Shuffles the cards. 
	 */
	public void ShuffleCards()
	{		
        for ( int i = 0; i < getDeckSize(); i++ )
        {
			int j = ( int ) ( Math.random( ) * 52 );
			String temp = CardDeck[ i ]; 
			CardDeck[ i ] = CardDeck[ j ];  
			CardDeck[ j ] = temp;
		} 
	}
}
