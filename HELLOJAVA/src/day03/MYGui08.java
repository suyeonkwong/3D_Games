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
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MYGui08 extends JFrame {

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
					MYGui08 frame = new MYGui08();
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
	public MYGui08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 451);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("\uB098:");
		lblMine.setBounds(35, 48, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("\uCEF4:");
		lblCom.setBounds(35, 95, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("\uACB0\uACFC:");
		lblResult.setBounds(35, 143, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == KeyEvent.VK_ENTER) {

					String arr[] = { "가위", "바위", "보" };
					
					String com = arr[(int) (Math.random() * 3)];
					tfCom.setText(com);
					
					if (tfMine.getText().equals("가위")) {
						if (tfCom.getText().equals("보")) {
							tfResult.setText("승리");
						} else if (tfCom.getText().equals("바위")) {
							tfResult.setText("패배");
						} else {
							tfResult.setText("비김");
						}
					} else if (tfMine.getText().equals("바위")) {
						if (tfCom.getText().equals("가위")) {
							tfResult.setText("승리");
						} else if (tfCom.getText().equals("보")) {
							tfResult.setText("패배");
						} else {
							tfResult.setText("비김");
						}
					} else if (tfMine.getText().equals("보")) {
						if (tfCom.getText().equals("바위")) {
							tfResult.setText("승리");
						} else if (tfCom.getText().equals("가위")) {
							tfResult.setText("패배");
						} else {
							tfResult.setText("비김");
						}
					}

				}
				
			}
		});
		tfMine.setBounds(136, 45, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(136, 92, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(136, 140, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("\uC2E4\uD589\uD558\uAE30");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String arr [] = {"가위", "바위", "보"};
				
				String com = arr[(int)(Math.random()*3)];
				tfCom.setText(com);
				
				if(tfMine.getText().equals("가위")) {
					if(tfCom.getText().equals("보")) {
						tfResult.setText("승리");
					}else if(tfCom.getText().equals("바위")) {
						tfResult.setText("패배");
					}else {
						tfResult.setText("비김");
					}
				}else if(tfMine.getText().equals("바위")) {
					if(tfCom.getText().equals("가위")) {
						tfResult.setText("승리");
					}else if(tfCom.getText().equals("보")) {
						tfResult.setText("패배");
					}else {
						tfResult.setText("비김");
					}
				}else if(tfMine.getText().equals("보")) {
					if(tfCom.getText().equals("바위")) {
						tfResult.setText("승리");
					}else if(tfCom.getText().equals("가위")) {
						tfResult.setText("패배");
					}else {
						tfResult.setText("비김");
					}
				}
				
			}
		});
		btn.setBounds(35, 186, 217, 23);
		contentPane.add(btn);
	}

}
