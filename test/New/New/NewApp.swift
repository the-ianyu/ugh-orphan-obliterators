//
//  NewApp.swift
//  New
//
//  Created by Ethan Loh on 17/9/2023.
//

import SwiftUI
import GoogleMaps
@main


struct NewApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
    if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
       // Use the appDelegate object to access the properties and
        GMSServices.provideAPIKey(AIzaSyAWCTXiGUKBZ9ebbWpyjH1k00V0Nzfev_0)
       methods of the app delegate.
    }
}
