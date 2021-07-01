package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MYGui06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MYGui06 frame = new MYGui06();
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
	public MYGui06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 288, 465);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("\uB2E8");
		lbl.setBounds(12, 10, 68, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(79, 7, 156, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JTextArea ta = new JTextArea(); //전역변수로 빼면 위로 안옮겨도 됨
		ta.setBounds(12, 81, 223, 304);
		contentPane.add(ta);
		JButton btn = new JButton("\uCD9C\uB825\uD558\uAE30");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int dan = Integer.parseInt(tf.getText());
				String result = "";
				
				
				for (int j = 1; j < 10; j++) {
					result += dan + "*" + j + "=" + (dan * j) + "\n";
				}

				ta.setText(result + "");
				
			}
		});
		btn.setBounds(12, 48, 226, 23);
		contentPane.add(btn);
		
	}
}
