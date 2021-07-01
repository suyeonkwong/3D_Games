package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MYGui04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MYGui04 frame = new MYGui04();
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
	public MYGui04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(25, 45, 67, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(104, 48, 57, 15);
		contentPane.add(lbl);
		
		tf2 = new JTextField();
		tf2.setBounds(131, 45, 57, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		tf3 = new JTextField();
		tf3.setBounds(275, 45, 83, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String a = tf1.getText();
				String b = tf2.getText();
				int sum = Integer.parseInt(a) + Integer.parseInt(b);
				tf3.setText(sum+"");
			}
		});
		btn.setBounds(200, 44, 57, 23);
		contentPane.add(btn);
		
		
		
		
		
	}

}
