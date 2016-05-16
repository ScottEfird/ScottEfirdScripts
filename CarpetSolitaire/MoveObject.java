import java.awt.*;
import java.awt.event.*;
import java.util.Map;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.*;
import javax.swing.event.*;

@SuppressWarnings("serial")
public class MoveObject extends JComponent {
	private Point startPoint;
	private Point resetPoint;
	private String cardName;
	private int location;
	private Deck moveObjectDeck;

	public MoveObject(JComponent component, int x, int y, Deck localDeck,
			int Location) {
		setCursor(new Cursor(Cursor.HAND_CURSOR));
		int X = x;
		int Y = y;
		setLocation(x, y);
		location = Location;
		moveObjectDeck = localDeck;
		setSize(component.getPreferredSize());
		setLayout(new BorderLayout());
		add(component);
		MouseInputAdapter listener = new Mouselistener();
		addMouseMotionListener(listener);
		addMouseListener(listener);
		checklocation(X, Y);
		setCardName(localDeck, location);

	}

	/**
	 * uses the mouse listener to capture the clicks and drags.
	 */
	private class Mouselistener extends MouseInputAdapter {
		@Override
		public void mousePressed(final MouseEvent e) {
			((JComponent) getParent()).setComponentZOrder(MoveObject.this, 0);
			repaint();
			startPoint = e.getPoint();
			resetPoint = getLocation();
		}

		@Override
		public void mouseDragged(final MouseEvent e) {
			int X = startPoint.x;
			int Y = startPoint.y;
			Point pointStart = getParent().getLocationOnScreen();
			Point pointDragged = e.getLocationOnScreen();
			Point position = new Point(pointDragged.x - pointStart.x - X,
					pointDragged.y - pointStart.y - Y);

			setLocation(position);
		}

		@Override
		public void mouseReleased(final MouseEvent e) {

			Point currentPoint = getLocation();			
			int Y = currentPoint.y;
			int X = currentPoint.x;

			String localString = getCardName();
			localString = localString.substring(0,
					Math.min(localString.length(), 3));

			if (((Y <= 35 && X <= 35) && (Y >= 05 && X >= 05))
					&& (localString.equals("ace"))) {
				Point snapSlot1 = new Point(20, 20);
				String testString = moveObjectDeck.lookForKey(snapSlot1);				
				if (testString.equals("none")) {
					makeStatic();
					setLocation(snapSlot1);
					updateLcoation(moveObjectDeck, getCardName(), snapSlot1);
				} else {
					setLocation(resetPoint);
					playSound();
				}
			} else if (((Y <= 142 && X <= 35) && (Y >= 112 && X >= 05))
					&& (localString.equals("ace"))) {
				Point snapSlot2 = new Point(20, 127);
				String testString = moveObjectDeck.lookForKey(snapSlot2);				
				if (testString.equals("none")) {
					makeStatic();
					setLocation(snapSlot2);
					updateLcoation(moveObjectDeck, getCardName(), snapSlot2);
				} else {
					setLocation(resetPoint);
					playSound();
				}
			} else if (((Y <= 249 && X <= 35) && (Y >= 219 && X >= 05))
					&& (localString.equals("ace"))) {
				Point snapSlot3 = new Point(20, 234);
				String testString = moveObjectDeck.lookForKey(snapSlot3);				
				if (testString.equals("none")) {
					makeStatic();
					setLocation(snapSlot3);
					updateLcoation(moveObjectDeck, getCardName(), snapSlot3);
				} else {
					setLocation(resetPoint);
					playSound();
				}
			} else if (((Y <= 356 && X <= 35) && (Y >= 326 && X >= 05))
					&& (localString.equals("ace"))) {
				Point snapSlot4 = new Point(20, 341);
				String testString = moveObjectDeck.lookForKey(snapSlot4);				
				if (testString.equals("none")) {
					makeStatic();
					setLocation(snapSlot4);
					updateLcoation(moveObjectDeck, getCardName(), snapSlot4);
				} else {
					setLocation(resetPoint);
					playSound();
				}
			} else {
				Point nullPoint = checkDefaultPoints(currentPoint);
				int nullY = nullPoint.y;
				int nullX = nullPoint.x;
				
				if(nullY == -999 && nullX == -999)
				{					
					setLocation(resetPoint);
					playSound();
				}
				else
				{
					String testString = moveObjectDeck.lookForKey(nullPoint);
					if (testString.equals("none")) {					

						Point leftCardPoint = new Point(nullX-78,nullY);	
						String leftCardName =  moveObjectDeck.lookForKey(leftCardPoint);	
						
						//If there is no card to the left
						if(leftCardName.equals("none"))
						{
							setLocation(resetPoint);
							playSound();
						}
						else
						{
							if(checkCardOrderLeft(leftCardName,cardName) == true)
							{
								setLocation(nullPoint);
								updateLcoation(moveObjectDeck, getCardName(), nullPoint);
							}
							else
							{
								setLocation(resetPoint);
								playSound();
							}							
						}				
					}
					else
					{
						setLocation(resetPoint);
						playSound();
					}
				}				
			}
		}

	};

	/**
	 * If we want a static card, pass it neg values of were you want it to go.
	 */
	private void checklocation(int X, int Y) {
		if (X < 0 && Y < 0) {
			makeStatic();
			int x = X * -1;
			int y = Y * -1;
			setLocation(x, y);
		}
	}
	
	/**
	 * Checks the name of two cards, gives a True if they are in order and
	 * a false if they are not in order.
	 */
	private Boolean checkCardOrderLeft(String leftCard, String rightCard)
	{
		if((leftCard.contains("Clubs") && (rightCard.contains("Clubs"))))
		{		
			for(int i = 0; i != moveObjectDeck.Clubs.length; i++)
			{
				if((moveObjectDeck.Clubs[i] == rightCard) && (moveObjectDeck.Clubs[i-1] == leftCard))
				{
					return true;
				}
			}
			return false;
		}
		else if((leftCard.contains("Diamonds") && (rightCard.contains("Diamonds"))))
		{
			for(int i = 0; i != moveObjectDeck.Diamonds.length; i++)
			{
				if((moveObjectDeck.Diamonds[i] == rightCard) && (moveObjectDeck.Diamonds[i-1] == leftCard))
				{
					return true;
				}
			}
			return false;
		}
		else if((leftCard.contains("Hearts") && (rightCard.contains("Hearts"))))
		{
			for(int i = 0; i != moveObjectDeck.Hearts.length; i++)
			{
				if((moveObjectDeck.Hearts[i] == rightCard) && (moveObjectDeck.Hearts[i-1] == leftCard))
				{
					return true;
				}
			}
			return false;
		}
		else if((leftCard.contains("Spades") && (rightCard.contains("Spades"))))
		{
			for(int i = 0; i != moveObjectDeck.Spades.length; i++)
			{
				if((moveObjectDeck.Spades[i] == rightCard) && (moveObjectDeck.Spades[i-1] == leftCard))
				{
					return true;
				}
			}
			return false;
		}
		else
		{
			return false;
		}
	}
	
	/**
	 * Checks the name of two cards, gives a True if they are in order and
	 * a false if they are not in order.
	 */
	private Boolean checkCardOrderRight(String leftCard, String rightCard)
		{
			if((leftCard.contains("Clubs") && (rightCard.contains("Clubs"))))
			{		
				for(int i = 0; i != moveObjectDeck.Clubs.length; i++)
				{
					if((moveObjectDeck.Clubs[i] == rightCard) && (moveObjectDeck.Clubs[i+1] == leftCard))
					{
						return true;
					}
				}
				return false;
			}
			else if((leftCard.contains("Diamonds") && (rightCard.contains("Diamonds"))))
			{
				for(int i = 0; i != moveObjectDeck.Diamonds.length; i++)
				{
					if((moveObjectDeck.Diamonds[i] == rightCard) && (moveObjectDeck.Diamonds[i+1] == leftCard))
					{
						return true;
					}
				}
				return false;
			}
			else if((leftCard.contains("Hearts") && (rightCard.contains("Hearts"))))
			{
				for(int i = 0; i != moveObjectDeck.Hearts.length; i++)
				{
					if((moveObjectDeck.Hearts[i] == rightCard) && (moveObjectDeck.Hearts[i+1] == leftCard))
					{
						return true;
					}
				}
				return false;
			}
			else if((leftCard.contains("Spades") && (rightCard.contains("Spades"))))
			{
				for(int i = 0; i != moveObjectDeck.Spades.length; i++)
				{
					if((moveObjectDeck.Spades[i] == rightCard) && (moveObjectDeck.Spades[i+1] == leftCard))
					{
						return true;
					}
				}
				return false;
			}
			else
			{
				return false;
			}
	}
		
	/**
	 * Updates the location of a card.
	 */
	private void updateLcoation(Deck localDeck, String keyName, Point location) {
		localDeck.setDeckMap(keyName, location);
		if(checkIfWon() == true)
		{
			JOptionPane.showMessageDialog (null, "You win!", "Message", JOptionPane.INFORMATION_MESSAGE);
		}		
	}

	/**
	 * Checks the default card spot array from the Deck class, if 
	 * it finds something with in an 15x15 box around the point it will
	 * return that new point, else it will return a null point with x and y=-999
	 */	
	private Point checkDefaultPoints(Point testPoint)
	{
		int Y = testPoint.y;
		int X = testPoint.x;
		
		for (Map.Entry<String, Point> entry : moveObjectDeck.getCardLocations().entrySet()) 
		{		    
		    //Checking each spot of the defaultCardMap
		    int currentPointX = entry.getValue().x;
		    int currentPointY = entry.getValue().y;
		    		    
		    if((Y <= (currentPointY + 15) && X <= (currentPointX + 15) && (Y >= (currentPointY - 15) && X >= (currentPointX - 15))))
		    {		    	
		    	return entry.getValue();
		    }	
		}
		    
		Point nullPoint = new Point(-999, -999);		
		return nullPoint;
	}

	/**
	 * Remove listener and make it static
	 */
	private void makeStatic() {
		for (MouseMotionListener listener : this.getMouseMotionListeners()) {
			removeMouseMotionListener(listener);
			removeMouseListener((MouseListener) listener);
		}
		setCursor(Cursor.getDefaultCursor());
	}

	/**
	 * Set the card name
	 */
	private void setCardName(Deck localDeck, int location) {
		if (location == -1) {
			cardName = "gray";
		} else {
			cardName = localDeck.getCard(location);
		}
	}

	private String getCardName() {
		return cardName;
	}

	/**
	 * Checks to see if you won after each move, checks the first row. If that row
	 * is correct moves onto the next row. Etc. if all four rows are correct, returns 
	 * true. Else, returns false. 
	 */
	private Boolean checkIfWon()
	{
		int X = 20;
		int Y = 20;
		
		String LeftRow1String, LeftRow2String, LeftRow3String, LeftRow4String;
		Point leftRow1Point = new Point(X,Y);
		Point leftRow2Point = new Point(X,Y);
		Point leftRow3Point = new Point(X,Y);
		Point leftRow4Point = new Point(X,Y);
		
		String RightRow1String, RightRow2String, RightRow3String, RightRow4String;
		Point rightRow1Point = new Point(X,Y);
		Point rightRow2Point = new Point(X,Y);
		Point rightRow3Point = new Point(X,Y);
		Point rightRow4Point = new Point(X,Y);
		
		
		X = 20;
		leftRow1Point.move(X,Y);
		LeftRow1String = moveObjectDeck.lookForKey(leftRow1Point);
		
		for(int i = 0; i != moveObjectDeck.Diamonds.length; i++)
		{
			X = X + 78;
			rightRow1Point.move(X,Y);
			RightRow1String = moveObjectDeck.lookForKey(rightRow1Point);
			
			if(checkCardOrderRight(LeftRow1String,RightRow1String) == true)
			{
				LeftRow1String = RightRow1String;				
			}
			else
			{
				return false;
			}
		}
		
		X = 20;
		Y = Y + 107;
		leftRow2Point.move(X,Y);
		LeftRow2String = moveObjectDeck.lookForKey(leftRow2Point);
		
		for(int i = 0; i != moveObjectDeck.Hearts.length; i++)
		{
			X = X + 78;
			rightRow2Point.move(X,Y);
			RightRow2String = moveObjectDeck.lookForKey(rightRow2Point);
			
			if(checkCardOrderRight(LeftRow2String,RightRow2String) == true)
			{
				LeftRow2String = RightRow2String;				
			}
			else
			{
				return false;
			}
		}
		
		X = 20;
		Y = Y + 107;
		leftRow3Point.move(X,Y);
		LeftRow3String = moveObjectDeck.lookForKey(leftRow3Point);
		
		for(int i = 0; i != moveObjectDeck.Hearts.length; i++)
		{
			X = X + 78;
			rightRow3Point.move(X,Y);
			RightRow3String = moveObjectDeck.lookForKey(rightRow3Point);
			
			if(checkCardOrderRight(LeftRow3String,RightRow3String) == true)
			{
				LeftRow3String = RightRow3String;				
			}
			else
			{
				return false;
			}
		}
		
		X = 20;
		Y = Y + 107;
		leftRow4Point.move(X,Y);
		LeftRow4String = moveObjectDeck.lookForKey(leftRow4Point);
		
		for(int i = 0; i != moveObjectDeck.Hearts.length; i++)
		{
			X = X + 78;
			rightRow4Point.move(X,Y);
			RightRow4String = moveObjectDeck.lookForKey(rightRow4Point);
			
			if(checkCardOrderRight(LeftRow4String,RightRow4String) == true)
			{
				LeftRow4String = RightRow4String;				
			}
			else
			{
				return false;
			}
		}
		
		//If all checks don't fail, you win!
		return true;

	}

	public static synchronized void playSound() {
		new Thread(new Runnable() {
		    public void run() {
		      try {
		        Clip clip = AudioSystem.getClip();
		        AudioInputStream inputStream = AudioSystem.getAudioInputStream(
		          Main.class.getResourceAsStream("src/images/beep.mp3"));
		        clip.open(inputStream);
		        clip.start(); 
		      } catch (Exception e) {
		        System.err.println(e.getMessage());
		      }
		    }
		  }).start();
		}


}
	
	




	
	
	
	
	
	
	
	






