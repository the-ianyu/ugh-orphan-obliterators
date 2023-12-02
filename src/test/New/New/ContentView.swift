//
//  ContentView.swift
//  New
//
//  Created by Ethan Loh on 17/9/2023.
//
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Button(action: {
                // Action for Button 1
                print("Button 1 tapped")
            }) {
                Text("Button 1")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }

            Button(action: {
                // Action for Button 2
                print("Button 2 tapped")
            }) {
                Text("Button 2")
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }

            Button(action: {
                // Action for Button 3
                print("Button 3 tapped")
            }) {
                Text("Button 3")
                    .padding()
                    .background(Color.orange)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }

            Button(action: {
                // Action for Button 4
                print("Button 4 tapped")
            }) {
                Text("Button 4")
                    .padding()
                    .background(Color.purple)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
