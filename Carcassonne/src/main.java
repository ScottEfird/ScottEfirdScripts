import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Image;
import java.awt.Point;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.ImageIcon;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class main {
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
				try {
					setDeck();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		});
	}

	
	/**
	 * Puts a card onto the frame.
	 * @throws IOException 
	 */
	public static void setDeck() throws IOException {
		BufferedImage myPicture = ImageIO.read(new File("src/images/1.png"));

		JLabel wIcon = new JLabel(new ImageIcon(myPicture));
		JPanel.add(wIcon);
		

	}
}

