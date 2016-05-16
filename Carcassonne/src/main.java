import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Image;
import java.awt.Point;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class main {
	public static JFrame frame;
	public static JPanel JPanel;

	public static void main(String[] args) {
		frame = new JFrame("Carcassonne");
		frame.setVisible(true);
		frame.setSize(1200, 600);
		frame.setLayout(new BorderLayout());
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
		JPanel = new JPanel();
		JPanel.setBackground(Color.decode("#64C866"));
		JPanel.setLayout(null);
		frame.add(JPanel, BorderLayout.CENTER);		
		
		java.awt.EventQueue.invokeLater(new Runnable() {
			public void run() {
				projectInit();
			}
		});
	}
	/**
	 * Generate names of files
	 */
	public static void projectInit() {
		JLabel imgLabel = new JLabel(new ImageIcon("src/images/1.png"));
		JPanel.add(imgLabel);
		JPanel.revalidate();
		JPanel.repaint();
		
		//Deck localDeck = new Deck();
	}
}
