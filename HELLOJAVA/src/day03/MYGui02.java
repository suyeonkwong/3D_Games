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

public class MYGui02 extends JFrame {

	private JPanel pan;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MYGui02 frame = new MYGui02();
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
	public MYGui02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		pan = new JPanel();
		pan.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(pan);
		pan.setLayout(null);
		
		JLabel lbl = new JLabel("10");
		lbl.setBounds(143, 100, 57, 15);
		pan.add(lbl);
		
		JButton btn = new JButton("increase");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String a = lbl.getText();
				int b = Integer.parseInt(a);
				b++;
				lbl.setText(Integer.toString(b));
			}
		});
		btn.setBounds(298, 142, 97, 23);
		pan.add(btn);
	}

}
