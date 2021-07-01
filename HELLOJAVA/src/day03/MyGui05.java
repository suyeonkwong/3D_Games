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

public class MyGui05 extends JFrame {

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
					MyGui05 frame = new MyGui05();
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
	public MyGui05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 25, 67, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl = new JLabel("\uC5D0\uC11C");
		lbl.setBounds(91, 28, 57, 15);
		contentPane.add(lbl);
		
		tf2 = new JTextField();
		tf2.setBounds(160, 25, 57, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JButton btn = new JButton("\uAE4C\uC9C0\uD569\uC740");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String a = tf1.getText();
				int a1 = Integer.parseInt(a);
				String b = tf2.getText();
				int b1 = Integer.parseInt(b);
				
				int sum = 0;
				
				for(int i=a1; i<b1+1; i++) {
					int result = sum += i;
					tf3.setText(Integer.toString(result));
				}
			}
		});
		btn.setBounds(229, 24, 99, 23);
		contentPane.add(btn);
		
		tf3 = new JTextField();
		tf3.setBounds(355, 25, 67, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
	}

}
