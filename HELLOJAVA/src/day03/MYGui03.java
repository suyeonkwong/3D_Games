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
import javax.swing.JTextField;

public class MYGui03 extends JFrame {

	private JPanel pan;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MYGui03 frame = new MYGui03();
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
	public MYGui03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		pan = new JPanel();
		pan.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(pan);
		pan.setLayout(null);
		
		tf = new JTextField();
		tf.setText("10");
		tf.setBounds(25, 45, 116, 21);
		pan.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("decrease");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String a = tf.getText();
				int b = Integer.parseInt(a);
				b--;
				tf.setText(Integer.toString(b));
			}
		});
		btn.setBounds(259, 127, 97, 23);
		pan.add(btn);
		
	}
}
