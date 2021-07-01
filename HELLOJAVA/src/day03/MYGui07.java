package day03;

import java.awt.BorderLayout;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MYGui07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MYGui07 frame = new MYGui07();
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
	public MYGui07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 267, 472);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("\uB098");
		lblMine.setBounds(12, 24, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("\uCEF4");
		lblCom.setBounds(12, 69, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("\uACB0\uACFC");
		lblResult.setBounds(12, 114, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == KeyEvent.VK_ENTER) {
					doGame();
				}
			}
		});
		tfMine.setBounds(111, 21, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(111, 66, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(111, 111, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("\uAC8C\uC784\uD558\uAE30");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				doGame();
				
			}
				
				

//				String mine = "";
//				String comp = "";
//				String result = "";
//				
//				mine = tfMine.getText();
//				double rnd = Math.random();
//				if(rnd > 0.5) {
//					comp = "È¦";
//				}else {
//					comp = "Â¦";
//				}
//				
//				if(comp.equals(mine)) {
//					result = "½Â¸®";
//				}else {
//					result = "ÆÐ¹è";
//				}
//				
//				tfCom.setText(comp);
//				tfResult.setText(result);
				
			
		});
		btn.setBounds(12, 166, 215, 23);
		contentPane.add(btn);
	}
	
	public void doGame() {
		String arr[] = { "È¦", "Â¦" };

		String com = arr[(int) (Math.random() * 2)];
		tfCom.setText(com);

		if (tfMine.getText().equals(tfCom.getText())) {
			tfResult.setText("½Â¸®");
		} else {
			tfResult.setText("ÆÐ¹è");
		}
	}

}
