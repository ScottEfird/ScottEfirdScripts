import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Image;
import java.awt.Point;
import java.awt.Toolkit;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Main {
	public static JFrame frame;
	public static JPanel JPanel;

	public static void main(String[] args) {
		frame = new JFrame("Carpet Solitaire");
		frame.setVisible(true);
		frame.setSize(1150, 495);
		frame.setLayout(new BorderLayout());
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
		JPanel = new JPanel();
		JPanel.setBackground(Color.decode("#64C866"));
		JPanel.setLayout(null);
		frame.add(JPanel, BorderLayout.CENTER);		
		
		java.awt.EventQueue.invokeLater(new Runnable() {
			public void run() {
				loadCards();
			}
		});
	}

	/**
	 * Generate names of files
	 */
	public static void loadCards() {		
		Deck localDeck = new Deck();
		localDeck.getDeck();
		localDeck.ShuffleCards();	
		setCards(localDeck);
	}
	
	
	/**
	 * Runs the loop to put the cards onto the board. 
	 */	
	public static void setCards(Deck localDeck)
	{
		int X = 20;
		int Y = 20;
		int A = 98;
		int B = 20;
		
		int count2 = 1;
		for (int j = 0; j != localDeck.getDeckSize(); j++) {
			if (count2 == 4) {
				setDeck(localDeck.getCard(j), A, B, localDeck, j);
				JPanel.repaint();
				B = 20;
				A = A + 78;
				count2 = 1;
			}
			// Next card
			else {
				if (j == 51) {
					setDeck(localDeck.getCard(0), A, B, localDeck, j);
					JPanel.repaint();
					B = B + 107;
				}

				setDeck(localDeck.getCard(j), A, B, localDeck, j);
				JPanel.repaint();
				B = B + 107;
				count2++;
			}
		}

		X = 20;
		Y = 20;
		int count = 0;
		for (int i = 0; i != localDeck.getDeckSize(); i++) {
			// For the starting row of Gray cards
			if (count == 0) {
				setGray(X, Y, localDeck);
				Y = Y + 107;
				setGray(X, Y, localDeck);
				Y = Y + 107;
				setGray(X, Y, localDeck);
				Y = Y + 107;
				setGray(X, Y, localDeck);
				Y = Y + 107;
				count = 1;
				Y = 20;
				X = 98;
				JPanel.repaint();
			}
			// New row of cards
			else if (count == 4) {
				setGray(X, Y, localDeck);
				JPanel.repaint();
				Y = 20;
				X = X + 78;
				count = 1;
			}
			// Next card
			else {
				// The loop never hits zero because of the gray row's count.
				// At the 51st card, put Deck[0] at 52nd spot.
				if (i == 51) {
					setGray(X, Y, localDeck);
					JPanel.repaint();
					Y = Y + 107;
				}
				JPanel.repaint();
				setGray(X, Y, localDeck);
				JPanel.repaint();
				Y = Y + 107;
				count++;
			}
		}
	}
	
	
	

	/**
	 * Puts a card onto the frame.
	 */
	public static void setDeck(String CardName, int X, int Y, Deck localDeck, int location) {
		
		Image image = Toolkit.getDefaultToolkit().getImage("src/images/" + CardName + ".gif" );
		ImageIcon icon = new ImageIcon(image);				
		JPanel.add(new MoveObject(new JLabel(icon),X,Y, localDeck, location));
		JPanel.revalidate();
		JPanel.repaint();
		
		Point position = new Point(X,Y);
		localDeck.setDeckMap(CardName,position);
		localDeck.setDefaultLocation(X,Y,location);			
	}

	/**
	 * Puts a gray card onto the board.
	 */		
	public static void setGray(int X, int Y, Deck localDeck) {
		Image image = Toolkit.getDefaultToolkit().createImage("src/images/gray.gif");
		ImageIcon icon = new ImageIcon(image);
		int x = X* -1;
		int y = Y* -1;		
		JPanel.add(new MoveObject(new JLabel(icon),x,y, localDeck, -1));
		JPanel.revalidate();
		JPanel.repaint();
	}
	

	
}














