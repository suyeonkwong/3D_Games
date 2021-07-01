package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MYGui01 extends JFrame {

	private JPanel pan;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MYGui01 frame = new MYGui01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MYGui01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300); //setSize¿Í ºñ½Á?
		pan = new JPanel();
		pan.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(pan);
		pan.setLayout(null);
		
		JLabel lbl = new JLabel("hello");
		lbl.setBounds(81, 53, 111, 83);
		pan.add(lbl);
		
		JButton btn = new JButton("Click");

		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lbl.setText("Good Moring");
			}
		});
		btn.setBounds(193, 53, 97, 23);
		pan.add(btn);
	}
}
